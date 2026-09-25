# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-25T15:07:31.910864+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0284` n `12`; crypto_alt avg `0.6196` n `234`; crypto_major avg `0.5648` n `8`; equity avg `0.3217` n `141`; fx avg `-0.0093` n `6`; index avg `0.0789` n `26`; metal avg `0.0876` n `20`; unknown avg `5.5271` n `958`
- 1h: commodity avg `0.0201` n `12`; crypto_alt avg `0.9559` n `234`; crypto_major avg `0.576` n `8`; equity avg `0.18` n `141`; fx avg `0.0076` n `6`; index avg `0.047` n `26`; metal avg `0.218` n `20`; unknown avg `15.0911` n `958`
- 4h: commodity avg `0.0237` n `12`; crypto_alt avg `-0.3941` n `234`; crypto_major avg `-0.7022` n `8`; equity avg `-0.9103` n `141`; fx avg `-0.0159` n `6`; index avg `-0.0523` n `26`; metal avg `-0.2098` n `20`; unknown avg `20.4877` n `916`
- 24h: commodity avg `-0.5922` n `12`; crypto_alt avg `2.8874` n `234`; crypto_major avg `1.8753` n `8`; equity avg `0.8294` n `141`; fx avg `-0.2431` n `6`; index avg `0.2557` n `26`; metal avg `0.2787` n `20`; unknown avg `15.9884` n `795`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1753`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1538`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1468`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1461`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1302`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1226`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0975`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
