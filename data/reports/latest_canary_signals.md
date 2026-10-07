# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-07T01:08:07.482662+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0957` n `13`; crypto_alt avg `-0.177` n `235`; crypto_major avg `-0.0763` n `8`; equity avg `-0.0924` n `150`; fx avg `-0.0224` n `6`; index avg `-0.0142` n `26`; metal avg `-0.0257` n `20`; unknown avg `0.2117` n `1074`
- 1h: commodity avg `0.1137` n `13`; crypto_alt avg `-0.0422` n `235`; crypto_major avg `0.0258` n `8`; equity avg `0.0119` n `150`; fx avg `-0.0191` n `6`; index avg `0.0178` n `26`; metal avg `-0.0508` n `20`; unknown avg `0.1968` n `1074`
- 4h: commodity avg `0.2105` n `13`; crypto_alt avg `-0.1445` n `235`; crypto_major avg `-0.1488` n `8`; equity avg `0.0072` n `150`; fx avg `-0.0016` n `6`; index avg `0.0094` n `26`; metal avg `-0.0549` n `20`; unknown avg `0.0806` n `1052`
- 24h: commodity avg `0.5038` n `13`; crypto_alt avg `-1.1351` n `235`; crypto_major avg `-1.1577` n `8`; equity avg `0.2818` n `149`; fx avg `0.0831` n `6`; index avg `-0.0055` n `26`; metal avg `-0.1076` n `20`; unknown avg `871.3863` n `914`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1638`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.151`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0837`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0779`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0769`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0738`, n `668`, weak_sample_signal
