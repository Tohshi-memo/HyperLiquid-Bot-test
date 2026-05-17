# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-17T21:37:12.071876+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.5789` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0223` n `12`; crypto_alt avg `0.1248` n `228`; crypto_major avg `0.0721` n `8`; equity avg `0.0221` n `65`; fx avg `0.0022` n `5`; index avg `0.0266` n `23`; metal avg `0.0467` n `18`; unknown avg `0.2423` n `384`
- 1h: commodity avg `-0.0727` n `12`; crypto_alt avg `0.3621` n `228`; crypto_major avg `0.3607` n `8`; equity avg `0.0862` n `65`; fx avg `-0.0279` n `5`; index avg `0.0352` n `23`; metal avg `0.0303` n `18`; unknown avg `0.2249` n `384`
- 4h: commodity avg `-0.0956` n `12`; crypto_alt avg `1.04` n `228`; crypto_major avg `1.4971` n `8`; equity avg `0.4798` n `65`; fx avg `-0.0262` n `5`; index avg `0.175` n `23`; metal avg `-0.0818` n `18`; unknown avg `0.5246` n `384`
- 24h: commodity avg `1.6632` n `12`; crypto_alt avg `-8.8639` n `228`; crypto_major avg `-1.1193` n `8`; equity avg `-2.1969` n `65`; fx avg `-0.1801` n `5`; index avg `-1.452` n `23`; metal avg `-5.916` n `18`; unknown avg `550.5792` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1367`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0839`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0777`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.075`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.069`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0678`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0505`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0495`, n `668`, weak_sample_signal
