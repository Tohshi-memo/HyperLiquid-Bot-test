# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T21:22:25.609277+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6058` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_crypto_metal_divergence: score `-1.5896` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_index_leads_crypto: score `1.4977` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0986` n `13`; crypto_alt avg `0.188` n `235`; crypto_major avg `0.0458` n `8`; equity avg `-0.0066` n `143`; fx avg `0.0667` n `6`; index avg `-0.0074` n `26`; metal avg `0.0079` n `20`; unknown avg `37.8455` n `984`
- 1h: commodity avg `0.0652` n `13`; crypto_alt avg `0.1753` n `235`; crypto_major avg `0.0187` n `8`; equity avg `-0.0072` n `143`; fx avg `0.0625` n `6`; index avg `-0.0101` n `26`; metal avg `-0.0157` n `20`; unknown avg `20.3134` n `970`
- 4h: commodity avg `0.3266` n `13`; crypto_alt avg `-2.7228` n `235`; crypto_major avg `-1.4764` n `8`; equity avg `0.1294` n `143`; fx avg `0.0366` n `6`; index avg `0.0213` n `26`; metal avg `0.1132` n `20`; unknown avg `5.6851` n `922`
- 24h: commodity avg `-0.0399` n `13`; crypto_alt avg `-1.4666` n `235`; crypto_major avg `-0.8704` n `8`; equity avg `0.7798` n `142`; fx avg `-0.0921` n `6`; index avg `0.2954` n `26`; metal avg `-0.2595` n `20`; unknown avg `-0.0524` n `802`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1651`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1428`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0981`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.092`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
