# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-26T10:22:30.798560+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0045` n `12`; crypto_alt avg `0.309` n `234`; crypto_major avg `0.1753` n `8`; equity avg `0.0171` n `141`; fx avg `0.0059` n `6`; index avg `-0.0058` n `26`; metal avg `0.0028` n `20`; unknown avg `1.1365` n `961`
- 1h: commodity avg `0.0185` n `12`; crypto_alt avg `0.7048` n `234`; crypto_major avg `0.321` n `8`; equity avg `0.0469` n `141`; fx avg `0.005` n `6`; index avg `-0.005` n `26`; metal avg `0.0013` n `20`; unknown avg `1.0122` n `959`
- 4h: commodity avg `-0.06` n `12`; crypto_alt avg `0.8266` n `234`; crypto_major avg `0.1436` n `8`; equity avg `0.0418` n `141`; fx avg `0.0269` n `6`; index avg `-0.0085` n `26`; metal avg `-0.0088` n `20`; unknown avg `-0.0099` n `943`
- 24h: commodity avg `0.0945` n `12`; crypto_alt avg `2.5895` n `234`; crypto_major avg `0.1238` n `8`; equity avg `-0.902` n `141`; fx avg `-0.0447` n `6`; index avg `-0.0071` n `26`; metal avg `-0.0936` n `20`; unknown avg `1121.5683` n `812`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1796`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1507`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1322`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1316`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0991`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0865`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.083`, n `668`, weak_sample_signal
