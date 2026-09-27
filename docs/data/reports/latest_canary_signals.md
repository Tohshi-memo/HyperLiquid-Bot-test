# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T01:52:30.160513+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- news_risk_spike: score `74.54` - News risk is high; compare crypto drawdown vs metal/index behavior.

## Class Returns

- 15m: commodity avg `-0.0008` n `12`; crypto_alt avg `0.2622` n `234`; crypto_major avg `0.2801` n `8`; equity avg `0.0449` n `141`; fx avg `0.0042` n `6`; index avg `-0.0013` n `26`; metal avg `0.0001` n `20`; unknown avg `1.1155` n `961`
- 1h: commodity avg `0.0074` n `12`; crypto_alt avg `0.4154` n `234`; crypto_major avg `0.3021` n `8`; equity avg `0.0118` n `141`; fx avg `-0.002` n `6`; index avg `0.0008` n `26`; metal avg `-0.0` n `20`; unknown avg `1.0469` n `959`
- 4h: commodity avg `-0.0664` n `12`; crypto_alt avg `0.4455` n `234`; crypto_major avg `0.3726` n `8`; equity avg `0.1027` n `141`; fx avg `-0.002` n `6`; index avg `0.0041` n `26`; metal avg `0.0011` n `20`; unknown avg `1.1537` n `927`
- 24h: commodity avg `-0.1081` n `12`; crypto_alt avg `0.7362` n `234`; crypto_major avg `-0.6378` n `8`; equity avg `0.2018` n `141`; fx avg `0.0159` n `6`; index avg `0.0004` n `26`; metal avg `-0.0058` n `20`; unknown avg `4.3245` n `884`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.175`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1556`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.155`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1483`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1386`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1221`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
