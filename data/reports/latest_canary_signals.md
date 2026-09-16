# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T22:22:26.521066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0202` n `12`; crypto_alt avg `0.0107` n `234`; crypto_major avg `0.005` n `8`; equity avg `0.1116` n `137`; fx avg `0.0091` n `6`; index avg `0.0177` n `27`; metal avg `-0.0089` n `20`; unknown avg `-0.2303` n `861`
- 1h: commodity avg `-0.0274` n `12`; crypto_alt avg `-0.4232` n `234`; crypto_major avg `-0.5223` n `8`; equity avg `0.18` n `137`; fx avg `0.0013` n `6`; index avg `0.0223` n `27`; metal avg `-0.0288` n `20`; unknown avg `0.7933` n `845`
- 4h: commodity avg `0.0078` n `12`; crypto_alt avg `0.2169` n `234`; crypto_major avg `-0.4429` n `8`; equity avg `-0.2437` n `137`; fx avg `0.0845` n `6`; index avg `-0.1557` n `27`; metal avg `-0.3621` n `20`; unknown avg `-0.577` n `761`
- 24h: commodity avg `-0.6236` n `12`; crypto_alt avg `0.5756` n `234`; crypto_major avg `0.7805` n `8`; equity avg `1.1195` n `137`; fx avg `0.0776` n `6`; index avg `0.0526` n `27`; metal avg `-0.3184` n `20`; unknown avg `-0.9412` n `723`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1185`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0824`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.081`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0654`, n `668`, weak_sample_signal
