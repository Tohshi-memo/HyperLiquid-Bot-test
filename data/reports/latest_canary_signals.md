# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-05T00:37:26.399953+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.23` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0115` n `12`; crypto_alt avg `0.0681` n `232`; crypto_major avg `-0.0307` n `8`; equity avg `-0.0151` n `134`; fx avg `-0.016` n `6`; index avg `-0.0075` n `26`; metal avg `-0.0017` n `20`; unknown avg `0.4541` n `784`
- 1h: commodity avg `-0.0421` n `12`; crypto_alt avg `0.155` n `232`; crypto_major avg `-0.0882` n `8`; equity avg `-0.0303` n `134`; fx avg `-0.0179` n `6`; index avg `0.0033` n `26`; metal avg `-0.001` n `20`; unknown avg `0.2467` n `758`
- 4h: commodity avg `-0.0296` n `12`; crypto_alt avg `0.3183` n `232`; crypto_major avg `-0.1436` n `8`; equity avg `0.0425` n `134`; fx avg `0.0149` n `6`; index avg `-0.041` n `26`; metal avg `-0.0066` n `20`; unknown avg `-0.2789` n `730`
- 24h: commodity avg `0.0028` n `12`; crypto_alt avg `-1.1514` n `232`; crypto_major avg `-2.4051` n `8`; equity avg `1.3076` n `134`; fx avg `-0.1317` n `6`; index avg `0.1497` n `26`; metal avg `-0.2646` n `20`; unknown avg `0.9482` n `652`

## Correlations

- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.1827`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1412`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1359`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1305`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1097`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1056`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0888`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0872`, n `668`, weak_sample_signal
