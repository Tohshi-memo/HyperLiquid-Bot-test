# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T06:07:36.832845+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0614` n `13`; crypto_alt avg `-0.4473` n `235`; crypto_major avg `-0.3434` n `8`; equity avg `-0.0028` n `149`; fx avg `-0.0207` n `6`; index avg `0.0038` n `26`; metal avg `-0.0652` n `20`; unknown avg `-0.0307` n `1040`
- 1h: commodity avg `-0.0667` n `13`; crypto_alt avg `-0.5389` n `235`; crypto_major avg `-0.5889` n `8`; equity avg `0.0054` n `149`; fx avg `-0.032` n `6`; index avg `0.0192` n `26`; metal avg `-0.0864` n `20`; unknown avg `-0.0996` n `1040`
- 4h: commodity avg `-0.0206` n `13`; crypto_alt avg `-0.554` n `235`; crypto_major avg `-0.533` n `8`; equity avg `0.0624` n `149`; fx avg `-0.0281` n `6`; index avg `0.024` n `26`; metal avg `-0.1615` n `20`; unknown avg `0.0172` n `1032`
- 24h: commodity avg `0.0053` n `13`; crypto_alt avg `-1.2881` n `235`; crypto_major avg `-0.6956` n `8`; equity avg `0.1859` n `149`; fx avg `0.0221` n `6`; index avg `0.1462` n `26`; metal avg `-0.1867` n `20`; unknown avg `587.2405` n `852`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1935`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1761`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1679`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.144`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1142`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1012`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.098`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0957`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0903`, n `668`, weak_sample_signal
