# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T09:36:25.787433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0458` n `12`; crypto_alt avg `0.0414` n `230`; crypto_major avg `0.0387` n `8`; equity avg `0.0728` n `102`; fx avg `0.0001` n `6`; index avg `0.0054` n `25`; metal avg `0.0045` n `20`; unknown avg `0.0154` n `782`
- 1h: commodity avg `-0.0669` n `12`; crypto_alt avg `0.0452` n `230`; crypto_major avg `-0.0074` n `8`; equity avg `-0.1219` n `102`; fx avg `0.0096` n `6`; index avg `-0.0159` n `25`; metal avg `-0.0102` n `20`; unknown avg `0.0806` n `782`
- 4h: commodity avg `-0.1606` n `12`; crypto_alt avg `0.026` n `230`; crypto_major avg `-0.271` n `8`; equity avg `0.135` n `102`; fx avg `-0.0203` n `6`; index avg `0.0194` n `25`; metal avg `-0.011` n `20`; unknown avg `-0.0226` n `766`
- 24h: commodity avg `-1.1956` n `12`; crypto_alt avg `0.3977` n `230`; crypto_major avg `0.3067` n `8`; equity avg `0.9395` n `102`; fx avg `-0.1462` n `6`; index avg `0.2498` n `25`; metal avg `0.2506` n `20`; unknown avg `0.3095` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1292`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1189`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0884`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0794`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0781`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0727`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0697`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
