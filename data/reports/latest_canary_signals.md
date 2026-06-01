# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T08:07:22.472014+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.0183` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.1325` n `12`; crypto_alt avg `-0.0688` n `228`; crypto_major avg `0.0999` n `8`; equity avg `-0.0783` n `69`; fx avg `-0.0052` n `6`; index avg `-0.5051` n `23`; metal avg `0.1269` n `18`; unknown avg `0.8331` n `422`
- 1h: commodity avg `0.0825` n `12`; crypto_alt avg `-0.6937` n `228`; crypto_major avg `-0.6737` n `8`; equity avg `-0.3199` n `69`; fx avg `0.0033` n `6`; index avg `-0.4202` n `23`; metal avg `-0.0765` n `18`; unknown avg `0.6939` n `422`
- 4h: commodity avg `0.3284` n `12`; crypto_alt avg `-2.0871` n `228`; crypto_major avg `-1.3146` n `8`; equity avg `-0.4282` n `69`; fx avg `-0.026` n `6`; index avg `-0.2963` n `23`; metal avg `-0.0582` n `18`; unknown avg `0.4421` n `412`
- 24h: commodity avg `1.2311` n `12`; crypto_alt avg `-0.7189` n `228`; crypto_major avg `-1.1983` n `8`; equity avg `-0.3207` n `69`; fx avg `-0.0082` n `6`; index avg `0.3976` n `23`; metal avg `0.0278` n `18`; unknown avg `1.3628` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2871`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2144`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2059`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1582`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1529`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1318`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.114`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1102`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1024`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0813`, n `668`, weak_sample_signal
