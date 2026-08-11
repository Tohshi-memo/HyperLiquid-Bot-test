# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T22:52:25.711107+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0087` n `12`; crypto_alt avg `-0.0464` n `230`; crypto_major avg `-0.0938` n `8`; equity avg `0.045` n `113`; fx avg `-0.0054` n `6`; index avg `0.0059` n `25`; metal avg `-0.0238` n `20`; unknown avg `1.7827` n `786`
- 1h: commodity avg `0.0305` n `12`; crypto_alt avg `0.0014` n `230`; crypto_major avg `-0.0205` n `8`; equity avg `0.0682` n `113`; fx avg `0.0077` n `6`; index avg `-0.0042` n `25`; metal avg `0.0199` n `20`; unknown avg `1.4312` n `786`
- 4h: commodity avg `-0.0002` n `12`; crypto_alt avg `0.5101` n `230`; crypto_major avg `0.8516` n `8`; equity avg `0.7252` n `113`; fx avg `0.0002` n `6`; index avg `0.0543` n `25`; metal avg `0.0192` n `20`; unknown avg `0.3724` n `785`
- 24h: commodity avg `0.1522` n `12`; crypto_alt avg `-1.0825` n `230`; crypto_major avg `0.6575` n `8`; equity avg `1.3232` n `113`; fx avg `-0.0661` n `6`; index avg `0.1138` n `25`; metal avg `-0.2416` n `20`; unknown avg `-0.1247` n `753`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2235`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2145`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2065`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.199`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1389`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1219`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
