# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T04:22:30.292922+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0255` n `13`; crypto_alt avg `0.0382` n `238`; crypto_major avg `0.0398` n `8`; equity avg `-0.0098` n `156`; fx avg `0.0107` n `6`; index avg `0.0259` n `27`; metal avg `0.0018` n `20`; unknown avg `-0.0008` n `1263`
- 1h: commodity avg `-0.1033` n `13`; crypto_alt avg `0.1534` n `238`; crypto_major avg `0.3959` n `8`; equity avg `0.3215` n `156`; fx avg `0.0094` n `6`; index avg `0.0786` n `27`; metal avg `0.0468` n `20`; unknown avg `1.6008` n `1201`
- 4h: commodity avg `-0.4848` n `13`; crypto_alt avg `0.7143` n `238`; crypto_major avg `1.1357` n `8`; equity avg `1.2678` n `156`; fx avg `0.1614` n `6`; index avg `0.2455` n `27`; metal avg `-0.0429` n `20`; unknown avg `2.2897` n `1193`
- 24h: commodity avg `-0.4839` n `13`; crypto_alt avg `-0.3629` n `238`; crypto_major avg `0.8574` n `8`; equity avg `1.5873` n `156`; fx avg `0.2154` n `6`; index avg `0.3829` n `27`; metal avg `0.0937` n `20`; unknown avg `3.4976` n `1074`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1827`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1755`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1463`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1369`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1355`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1338`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1198`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
