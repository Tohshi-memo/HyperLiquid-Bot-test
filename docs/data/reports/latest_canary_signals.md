# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-03T10:22:27.363706+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0881` n `12`; crypto_alt avg `0.109` n `232`; crypto_major avg `0.1001` n `8`; equity avg `-0.0644` n `133`; fx avg `0.0021` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0564` n `20`; unknown avg `-0.1281` n `792`
- 1h: commodity avg `0.2343` n `12`; crypto_alt avg `-0.0403` n `232`; crypto_major avg `-0.0718` n `8`; equity avg `-0.1795` n `133`; fx avg `-0.0219` n `6`; index avg `-0.0726` n `26`; metal avg `-0.1365` n `20`; unknown avg `0.5601` n `790`
- 4h: commodity avg `0.4414` n `12`; crypto_alt avg `0.2078` n `232`; crypto_major avg `0.0076` n `8`; equity avg `-0.2074` n `133`; fx avg `-0.0928` n `6`; index avg `-0.0801` n `26`; metal avg `-0.0276` n `20`; unknown avg `-0.0225` n `788`
- 24h: commodity avg `0.5723` n `12`; crypto_alt avg `2.0232` n `232`; crypto_major avg `1.8066` n `8`; equity avg `1.525` n `133`; fx avg `-0.4056` n `6`; index avg `0.1298` n `26`; metal avg `0.7584` n `20`; unknown avg `-0.2036` n `735`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0832`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.0754`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.0649`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0515`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0497`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0454`, n `668`, weak_sample_signal
