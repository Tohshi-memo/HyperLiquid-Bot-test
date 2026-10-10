# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-10T16:37:24.999216+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0662` n `13`; crypto_alt avg `-0.026` n `235`; crypto_major avg `-0.0732` n `8`; equity avg `-0.0092` n `150`; fx avg `0.0006` n `6`; index avg `-0.0026` n `26`; metal avg `0.0003` n `20`; unknown avg `-0.2857` n `1117`
- 1h: commodity avg `-0.0091` n `13`; crypto_alt avg `0.1427` n `235`; crypto_major avg `-0.2124` n `8`; equity avg `-0.0149` n `150`; fx avg `0.0` n `6`; index avg `-0.0028` n `26`; metal avg `-0.0164` n `20`; unknown avg `6.7585` n `1109`
- 4h: commodity avg `0.0321` n `13`; crypto_alt avg `0.9644` n `235`; crypto_major avg `0.4273` n `8`; equity avg `0.1038` n `150`; fx avg `-0.0077` n `6`; index avg `0.0164` n `26`; metal avg `-0.0103` n `20`; unknown avg `0.8623` n `1101`
- 24h: commodity avg `-0.4473` n `13`; crypto_alt avg `2.5555` n `235`; crypto_major avg `0.85` n `8`; equity avg `0.3042` n `150`; fx avg `0.019` n `6`; index avg `0.0515` n `26`; metal avg `0.0327` n `20`; unknown avg `1.3962` n `984`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1566`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1465`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1248`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1051`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.105`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0952`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0878`, n `668`, weak_sample_signal
