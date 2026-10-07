# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T18:52:33.136851+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0197` n `13`; crypto_alt avg `0.1828` n `235`; crypto_major avg `0.2096` n `8`; equity avg `0.057` n `150`; fx avg `-0.0013` n `6`; index avg `0.0042` n `26`; metal avg `0.0074` n `20`; unknown avg `1.9342` n `1077`
- 1h: commodity avg `0.2842` n `13`; crypto_alt avg `0.7132` n `235`; crypto_major avg `0.4763` n `8`; equity avg `0.1272` n `150`; fx avg `0.0082` n `6`; index avg `0.0172` n `26`; metal avg `0.0017` n `20`; unknown avg `0.6858` n `1075`
- 4h: commodity avg `-0.4147` n `13`; crypto_alt avg `0.9448` n `235`; crypto_major avg `0.2532` n `8`; equity avg `0.3608` n `150`; fx avg `-0.0117` n `6`; index avg `0.1324` n `26`; metal avg `0.0507` n `20`; unknown avg `1.6928` n `1068`
- 24h: commodity avg `0.3183` n `13`; crypto_alt avg `-4.6823` n `235`; crypto_major avg `-3.4505` n `8`; equity avg `-1.4604` n `150`; fx avg `-0.1781` n `6`; index avg `-0.2353` n `26`; metal avg `-0.7001` n `20`; unknown avg `15.4342` n `988`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1444`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0803`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0663`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0642`, n `668`, weak_sample_signal
