# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-26T17:22:47.591621+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0354` n `12`; crypto_alt avg `0.4528` n `231`; crypto_major avg `0.3704` n `8`; equity avg `0.1479` n `122`; fx avg `-0.0092` n `6`; index avg `0.0212` n `25`; metal avg `0.0005` n `20`; unknown avg `0.0613` n `797`
- 1h: commodity avg `-0.0931` n `12`; crypto_alt avg `0.5029` n `231`; crypto_major avg `0.3511` n `8`; equity avg `0.198` n `122`; fx avg `-0.0102` n `6`; index avg `0.0243` n `25`; metal avg `-0.0114` n `20`; unknown avg `0.0619` n `797`
- 4h: commodity avg `0.4781` n `12`; crypto_alt avg `-0.4938` n `231`; crypto_major avg `-0.1785` n `8`; equity avg `0.3464` n `122`; fx avg `-0.0107` n `6`; index avg `0.0475` n `25`; metal avg `-0.1825` n `20`; unknown avg `-0.0977` n `797`
- 24h: commodity avg `0.3529` n `12`; crypto_alt avg `-1.6784` n `231`; crypto_major avg `-1.729` n `8`; equity avg `-0.209` n `122`; fx avg `-0.0516` n `6`; index avg `0.0357` n `25`; metal avg `-0.3072` n `20`; unknown avg `0.4808` n `779`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1657`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.131`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0983`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0921`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0883`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0812`, n `668`, weak_sample_signal
