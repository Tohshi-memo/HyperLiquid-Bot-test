# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T10:22:30.139227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.9917` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.02` n `12`; crypto_alt avg `-0.3004` n `231`; crypto_major avg `-0.3079` n `8`; equity avg `-0.0679` n `127`; fx avg `-0.0042` n `6`; index avg `-0.0037` n `26`; metal avg `0.0433` n `20`; unknown avg `0.1977` n `792`
- 1h: commodity avg `0.0453` n `12`; crypto_alt avg `-0.6054` n `231`; crypto_major avg `-0.3505` n `8`; equity avg `-0.0688` n `127`; fx avg `0.0093` n `6`; index avg `-0.0065` n `26`; metal avg `-0.0619` n `20`; unknown avg `0.3407` n `792`
- 4h: commodity avg `0.1284` n `12`; crypto_alt avg `1.3691` n `231`; crypto_major avg `1.7914` n `8`; equity avg `0.7511` n `127`; fx avg `-0.0129` n `6`; index avg `0.073` n `26`; metal avg `-0.2003` n `20`; unknown avg `0.2888` n `791`
- 24h: commodity avg `0.512` n `12`; crypto_alt avg `1.8055` n `231`; crypto_major avg `2.4982` n `8`; equity avg `2.0039` n `127`; fx avg `-0.0765` n `6`; index avg `0.3105` n `26`; metal avg `-0.3988` n `20`; unknown avg `0.4942` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1233`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1037`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0935`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0757`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0681`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0679`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
