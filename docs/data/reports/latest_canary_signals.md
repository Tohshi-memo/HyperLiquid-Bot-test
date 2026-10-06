# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-06T12:52:34.112844+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.028` n `13`; crypto_alt avg `0.0784` n `235`; crypto_major avg `0.1044` n `8`; equity avg `0.0968` n `150`; fx avg `-0.0223` n `6`; index avg `0.0114` n `26`; metal avg `-0.0001` n `20`; unknown avg `0.255` n `1074`
- 1h: commodity avg `-0.0659` n `13`; crypto_alt avg `-0.1075` n `235`; crypto_major avg `-0.0825` n `8`; equity avg `-0.0166` n `150`; fx avg `-0.0076` n `6`; index avg `-0.0227` n `26`; metal avg `-0.1129` n `20`; unknown avg `0.7009` n `1064`
- 4h: commodity avg `-0.2658` n `13`; crypto_alt avg `0.4298` n `235`; crypto_major avg `0.3104` n `8`; equity avg `0.3922` n `149`; fx avg `0.0667` n `6`; index avg `0.0766` n `26`; metal avg `0.0065` n `20`; unknown avg `0.4962` n `1064`
- 24h: commodity avg `-0.7591` n `13`; crypto_alt avg `-0.1865` n `235`; crypto_major avg `0.1676` n `8`; equity avg `0.9179` n `149`; fx avg `0.0716` n `6`; index avg `0.2968` n `26`; metal avg `-0.0821` n `20`; unknown avg `0.2674` n `874`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.17`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1536`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1454`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1272`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0927`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0858`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0842`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0739`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.07`, n `668`, weak_sample_signal
