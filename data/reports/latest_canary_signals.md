# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T07:07:28.804779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0081` n `12`; crypto_alt avg `0.1277` n `234`; crypto_major avg `0.128` n `8`; equity avg `0.1801` n `137`; fx avg `-0.0028` n `6`; index avg `0.0367` n `27`; metal avg `0.0434` n `20`; unknown avg `0.0074` n `919`
- 1h: commodity avg `-0.0639` n `12`; crypto_alt avg `0.4005` n `234`; crypto_major avg `0.3364` n `8`; equity avg `0.3896` n `137`; fx avg `-0.0097` n `6`; index avg `0.0996` n `27`; metal avg `0.0443` n `20`; unknown avg `0.0351` n `919`
- 4h: commodity avg `-0.2429` n `12`; crypto_alt avg `0.8584` n `234`; crypto_major avg `0.1727` n `8`; equity avg `0.2928` n `137`; fx avg `0.0287` n `6`; index avg `0.06` n `27`; metal avg `0.1757` n `20`; unknown avg `0.0803` n `891`
- 24h: commodity avg `-0.5039` n `12`; crypto_alt avg `2.6716` n `234`; crypto_major avg `1.3152` n `8`; equity avg `1.0078` n `137`; fx avg `0.047` n `6`; index avg `0.085` n `27`; metal avg `-0.1715` n `20`; unknown avg `0.323` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1199`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1039`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1016`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1013`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0992`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0817`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0768`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0762`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0741`, n `668`, weak_sample_signal
