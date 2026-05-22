# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T19:07:21.049269+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `-1.8065` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.7673` - Index perps are stronger than crypto majors; possible risk-on canary.
- 1h_index_leads_crypto: score `1.1187` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.1454` n `12`; crypto_alt avg `-0.451` n `228`; crypto_major avg `-0.3861` n `8`; equity avg `-0.2004` n `67`; fx avg `0.0258` n `6`; index avg `-0.0433` n `23`; metal avg `-0.1411` n `18`; unknown avg `-0.142` n `386`
- 1h: commodity avg `0.0975` n `12`; crypto_alt avg `-1.76` n `228`; crypto_major avg `-1.225` n `8`; equity avg `-0.4618` n `67`; fx avg `0.0327` n `6`; index avg `-0.1063` n `23`; metal avg `-0.148` n `18`; unknown avg `0.0421` n `386`
- 4h: commodity avg `-0.5248` n `12`; crypto_alt avg `-2.194` n `228`; crypto_major avg `-1.694` n `8`; equity avg `-0.5503` n `67`; fx avg `0.0712` n `6`; index avg `0.0733` n `23`; metal avg `0.1125` n `18`; unknown avg `-0.44` n `386`
- 24h: commodity avg `-1.0031` n `12`; crypto_alt avg `-2.0655` n `228`; crypto_major avg `-1.7844` n `8`; equity avg `-0.3348` n `67`; fx avg `0.1736` n `6`; index avg `0.9066` n `23`; metal avg `-0.6653` n `18`; unknown avg `-0.8594` n `376`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0673`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0531`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0479`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.046`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0455`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.043`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0427`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0413`, n `668`, weak_sample_signal
