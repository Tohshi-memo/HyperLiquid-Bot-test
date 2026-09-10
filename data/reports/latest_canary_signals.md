# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T18:07:30.308779+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1011` n `12`; crypto_alt avg `-0.44` n `233`; crypto_major avg `-0.3915` n `8`; equity avg `-0.1173` n `135`; fx avg `0.0002` n `6`; index avg `-0.0066` n `26`; metal avg `-0.0475` n `20`; unknown avg `0.2406` n `795`
- 1h: commodity avg `0.1748` n `12`; crypto_alt avg `0.016` n `233`; crypto_major avg `0.1155` n `8`; equity avg `-0.2073` n `135`; fx avg `-0.0039` n `6`; index avg `-0.049` n `26`; metal avg `-0.0935` n `20`; unknown avg `0.0293` n `794`
- 4h: commodity avg `0.5602` n `12`; crypto_alt avg `-0.0757` n `233`; crypto_major avg `0.0032` n `8`; equity avg `0.0051` n `135`; fx avg `0.0522` n `6`; index avg `-0.0087` n `26`; metal avg `-0.2049` n `20`; unknown avg `-0.302` n `760`
- 24h: commodity avg `1.0061` n `12`; crypto_alt avg `-4.4728` n `233`; crypto_major avg `-3.6434` n `8`; equity avg `-2.0996` n `135`; fx avg `0.0966` n `6`; index avg `-0.3256` n `26`; metal avg `-1.2832` n `20`; unknown avg `-0.7252` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1254`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1048`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0863`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0856`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0819`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0817`, n `668`, weak_sample_signal
