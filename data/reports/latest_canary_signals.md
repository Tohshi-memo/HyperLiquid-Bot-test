# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-02T20:22:32.054601+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.87` - Polymarket crypto volume is unusually high.
- 4h_index_leads_crypto: score `1.7383` - Index perps are stronger than crypto majors; possible risk-on canary.
- 4h_crypto_equity_divergence: score `-1.6569` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0072` n `12`; crypto_alt avg `-0.9377` n `228`; crypto_major avg `-0.7877` n `8`; equity avg `0.1493` n `69`; fx avg `0.0` n `6`; index avg `-0.0788` n `23`; metal avg `0.0176` n `18`; unknown avg `-0.4416` n `422`
- 1h: commodity avg `0.0159` n `12`; crypto_alt avg `-0.3886` n `228`; crypto_major avg `-0.4906` n `8`; equity avg `0.2842` n `69`; fx avg `0.0061` n `6`; index avg `0.0941` n `23`; metal avg `0.0839` n `18`; unknown avg `-0.3543` n `422`
- 4h: commodity avg `0.2034` n `12`; crypto_alt avg `-1.4008` n `228`; crypto_major avg `-1.6152` n `8`; equity avg `0.0417` n `69`; fx avg `-0.0118` n `6`; index avg `0.1231` n `23`; metal avg `-0.2324` n `18`; unknown avg `-0.9782` n `422`
- 24h: commodity avg `-0.0032` n `12`; crypto_alt avg `-4.7502` n `228`; crypto_major avg `-5.4407` n `8`; equity avg `0.9254` n `69`; fx avg `0.0936` n `6`; index avg `0.5795` n `23`; metal avg `0.4369` n `18`; unknown avg `-0.5458` n `412`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1782`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0959`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0763`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.0754`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0737`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
