# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T01:22:28.841676+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0029` n `13`; crypto_alt avg `-0.1479` n `235`; crypto_major avg `-0.1752` n `8`; equity avg `-0.0764` n `150`; fx avg `-0.0092` n `6`; index avg `-0.014` n `26`; metal avg `-0.0202` n `20`; unknown avg `-0.0474` n `1076`
- 1h: commodity avg `0.0849` n `13`; crypto_alt avg `-0.0957` n `235`; crypto_major avg `-0.1243` n `8`; equity avg `-0.2106` n `150`; fx avg `-0.0483` n `6`; index avg `-0.0297` n `26`; metal avg `-0.0823` n `20`; unknown avg `-0.0439` n `1074`
- 4h: commodity avg `0.2513` n `13`; crypto_alt avg `-0.1617` n `235`; crypto_major avg `-0.2098` n `8`; equity avg `-0.0354` n `150`; fx avg `-0.0105` n `6`; index avg `0.0002` n `26`; metal avg `-0.0823` n `20`; unknown avg `0.0564` n `1052`
- 24h: commodity avg `0.4756` n `13`; crypto_alt avg `-1.0197` n `235`; crypto_major avg `-1.1317` n `8`; equity avg `0.3615` n `149`; fx avg `0.0447` n `6`; index avg `0.0201` n `26`; metal avg `-0.0346` n `20`; unknown avg `871.2922` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.162`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1492`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1476`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0829`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0765`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0745`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0736`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0716`, n `668`, weak_sample_signal
