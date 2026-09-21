# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-21T06:37:27.937209+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0102` n `12`; crypto_alt avg `-0.0037` n `234`; crypto_major avg `-0.2028` n `8`; equity avg `0.026` n `140`; fx avg `-0.0203` n `6`; index avg `0.02` n `26`; metal avg `0.0018` n `20`; unknown avg `1.9556` n `936`
- 1h: commodity avg `-0.066` n `12`; crypto_alt avg `0.3027` n `234`; crypto_major avg `0.0989` n `8`; equity avg `0.1288` n `140`; fx avg `-0.0491` n `6`; index avg `0.0377` n `26`; metal avg `-0.0138` n `20`; unknown avg `1.886` n `904`
- 4h: commodity avg `0.0434` n `12`; crypto_alt avg `1.7148` n `234`; crypto_major avg `0.5012` n `8`; equity avg `0.1676` n `140`; fx avg `-0.0398` n `6`; index avg `0.067` n `26`; metal avg `-0.101` n `20`; unknown avg `44.6606` n `898`
- 24h: commodity avg `-0.6118` n `12`; crypto_alt avg `4.0255` n `234`; crypto_major avg `2.8387` n `8`; equity avg `1.1924` n `140`; fx avg `-0.0573` n `6`; index avg `0.2592` n `26`; metal avg `-0.0316` n `20`; unknown avg `3.6771` n `767`

## Correlations

- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1774`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.152`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1466`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0957`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0906`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0873`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.085`, n `668`, weak_sample_signal
