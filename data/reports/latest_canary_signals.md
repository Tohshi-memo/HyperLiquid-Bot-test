# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-22T16:37:15.635712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5253` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1095` n `12`; crypto_alt avg `-0.0148` n `228`; crypto_major avg `0.074` n `8`; equity avg `0.0281` n `67`; fx avg `0.0173` n `6`; index avg `0.0571` n `23`; metal avg `0.1055` n `18`; unknown avg `-0.0826` n `386`
- 1h: commodity avg `-0.1847` n `12`; crypto_alt avg `-0.1862` n `228`; crypto_major avg `-0.1544` n `8`; equity avg `0.0379` n `67`; fx avg `0.0501` n `6`; index avg `0.0508` n `23`; metal avg `0.1198` n `18`; unknown avg `-0.8037` n `386`
- 4h: commodity avg `-0.3543` n `12`; crypto_alt avg `-1.1701` n `228`; crypto_major avg `-1.1392` n `8`; equity avg `-0.129` n `67`; fx avg `0.0532` n `6`; index avg `0.3861` n `23`; metal avg `0.2279` n `18`; unknown avg `-0.5261` n `386`
- 24h: commodity avg `-2.0346` n `12`; crypto_alt avg `0.9142` n `228`; crypto_major avg `-0.0775` n `8`; equity avg `0.8051` n `67`; fx avg `0.1797` n `6`; index avg `1.2866` n `23`; metal avg `-0.1188` n `18`; unknown avg `-0.726` n `375`

## Correlations

- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0722`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0507`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0503`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.0431`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0405`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0397`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0392`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0387`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0366`, n `668`, weak_sample_signal
