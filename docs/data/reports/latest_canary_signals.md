# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-12T07:22:27.495927+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0053` n `12`; crypto_alt avg `-0.0375` n `230`; crypto_major avg `-0.0176` n `8`; equity avg `0.0165` n `113`; fx avg `0.0005` n `6`; index avg `-0.0069` n `25`; metal avg `-0.0081` n `20`; unknown avg `-0.0183` n `786`
- 1h: commodity avg `-0.0056` n `12`; crypto_alt avg `-0.1686` n `230`; crypto_major avg `0.1513` n `8`; equity avg `0.239` n `113`; fx avg `0.0265` n `6`; index avg `0.0271` n `25`; metal avg `0.0907` n `20`; unknown avg `-0.0091` n `786`
- 4h: commodity avg `-0.015` n `12`; crypto_alt avg `-0.5299` n `230`; crypto_major avg `-0.0516` n `8`; equity avg `0.0676` n `113`; fx avg `0.0015` n `6`; index avg `-0.0204` n `25`; metal avg `0.0329` n `20`; unknown avg `-0.0481` n `770`
- 24h: commodity avg `-0.0812` n `12`; crypto_alt avg `-0.9001` n `230`; crypto_major avg `1.0037` n `8`; equity avg `2.1491` n `113`; fx avg `0.0232` n `6`; index avg `0.2119` n `25`; metal avg `0.2736` n `20`; unknown avg `-0.0849` n `769`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.2275`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.2227`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.2107`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.2087`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1821`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1395`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1111`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1096`, n `668`, weak_sample_signal
