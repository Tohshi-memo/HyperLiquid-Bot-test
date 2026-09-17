# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T04:37:34.620522+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0028` n `12`; crypto_alt avg `0.1374` n `234`; crypto_major avg `0.0197` n `8`; equity avg `-0.0263` n `137`; fx avg `0.0058` n `6`; index avg `-0.0117` n `27`; metal avg `-0.0043` n `20`; unknown avg `0.4551` n `915`
- 1h: commodity avg `0.0528` n `12`; crypto_alt avg `-0.1151` n `234`; crypto_major avg `-0.3944` n `8`; equity avg `0.0873` n `137`; fx avg `0.0045` n `6`; index avg `0.0094` n `27`; metal avg `0.0171` n `20`; unknown avg `0.2555` n `913`
- 4h: commodity avg `0.199` n `12`; crypto_alt avg `0.4802` n `234`; crypto_major avg `0.1679` n `8`; equity avg `0.1469` n `137`; fx avg `0.037` n `6`; index avg `0.0138` n `27`; metal avg `0.1898` n `20`; unknown avg `0.0298` n `911`
- 24h: commodity avg `-0.3364` n `12`; crypto_alt avg `1.6949` n `234`; crypto_major avg `0.7839` n `8`; equity avg `1.152` n `137`; fx avg `0.0295` n `6`; index avg `0.1094` n `27`; metal avg `-0.2199` n `20`; unknown avg `0.4703` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1373`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.117`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1073`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0942`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0838`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0746`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0721`, n `668`, weak_sample_signal
