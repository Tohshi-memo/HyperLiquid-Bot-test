# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-23T18:22:28.278243+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `12`; crypto_alt avg `-0.4199` n `234`; crypto_major avg `-0.3475` n `8`; equity avg `0.0246` n `141`; fx avg `-0.0096` n `6`; index avg `0.0042` n `26`; metal avg `-0.0282` n `20`; unknown avg `10.9095` n `943`
- 1h: commodity avg `0.1124` n `12`; crypto_alt avg `-0.6561` n `234`; crypto_major avg `-0.4472` n `8`; equity avg `0.1232` n `141`; fx avg `-0.0165` n `6`; index avg `0.0354` n `26`; metal avg `0.0626` n `20`; unknown avg `10.5768` n `941`
- 4h: commodity avg `0.1347` n `12`; crypto_alt avg `-0.8776` n `234`; crypto_major avg `-0.4994` n `8`; equity avg `0.4259` n `141`; fx avg `-0.0442` n `6`; index avg `0.0145` n `26`; metal avg `-0.0036` n `20`; unknown avg `3.7809` n `919`
- 24h: commodity avg `0.4838` n `12`; crypto_alt avg `-3.2725` n `234`; crypto_major avg `-3.8558` n `8`; equity avg `-1.3088` n `140`; fx avg `-0.0137` n `6`; index avg `-0.353` n `26`; metal avg `-0.7856` n `20`; unknown avg `17.1784` n `878`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1464`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1458`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.132`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1169`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1117`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1057`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1021`, n `668`, weak_sample_signal
