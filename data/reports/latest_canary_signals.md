# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T03:37:29.352571+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0429` n `12`; crypto_alt avg `0.2394` n `234`; crypto_major avg `0.1657` n `8`; equity avg `0.0432` n `137`; fx avg `0.0055` n `6`; index avg `0.0111` n `27`; metal avg `0.0608` n `20`; unknown avg `-0.2936` n `921`
- 1h: commodity avg `0.0461` n `12`; crypto_alt avg `0.2987` n `234`; crypto_major avg `0.2472` n `8`; equity avg `0.0867` n `137`; fx avg `-0.0129` n `6`; index avg `0.0152` n `27`; metal avg `0.1006` n `20`; unknown avg `-0.1913` n `918`
- 4h: commodity avg `0.0497` n `12`; crypto_alt avg `0.9793` n `234`; crypto_major avg `0.7436` n `8`; equity avg `0.2354` n `137`; fx avg `0.0223` n `6`; index avg `0.0634` n `27`; metal avg `0.2658` n `20`; unknown avg `0.4787` n `909`
- 24h: commodity avg `-0.4429` n `12`; crypto_alt avg `2.296` n `234`; crypto_major avg `1.5035` n `8`; equity avg `1.1721` n `137`; fx avg `0.0071` n `6`; index avg `0.1043` n `27`; metal avg `-0.2123` n `20`; unknown avg `1.2208` n `715`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1367`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1166`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1082`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1072`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0945`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0834`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0776`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
