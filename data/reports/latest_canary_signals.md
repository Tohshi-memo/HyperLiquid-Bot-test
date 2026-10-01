# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-01T07:22:32.435441+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1289` n `13`; crypto_alt avg `-0.6874` n `234`; crypto_major avg `-0.6582` n `8`; equity avg `-0.338` n `142`; fx avg `0.0153` n `6`; index avg `-0.0976` n `26`; metal avg `-0.1446` n `20`; unknown avg `1.5377` n `975`
- 1h: commodity avg `0.4261` n `13`; crypto_alt avg `-0.6443` n `234`; crypto_major avg `-0.7097` n `8`; equity avg `-0.5697` n `142`; fx avg `0.0377` n `6`; index avg `-0.1618` n `26`; metal avg `-0.2617` n `20`; unknown avg `2.9882` n `972`
- 4h: commodity avg `0.1268` n `13`; crypto_alt avg `0.0048` n `234`; crypto_major avg `0.104` n `8`; equity avg `0.2095` n `142`; fx avg `0.0198` n `6`; index avg `0.0008` n `26`; metal avg `-0.0833` n `20`; unknown avg `0.2191` n `940`
- 24h: commodity avg `0.307` n `13`; crypto_alt avg `1.0693` n `234`; crypto_major avg `0.8776` n `8`; equity avg `0.4611` n `142`; fx avg `0.1832` n `6`; index avg `0.091` n `26`; metal avg `-0.3685` n `20`; unknown avg `774.2089` n `794`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1313`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1252`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1203`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0927`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0908`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
