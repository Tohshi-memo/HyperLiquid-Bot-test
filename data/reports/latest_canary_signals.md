# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-29T10:07:29.730222+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0522` n `12`; crypto_alt avg `0.0252` n `234`; crypto_major avg `-0.0412` n `8`; equity avg `0.0735` n `141`; fx avg `0.0105` n `6`; index avg `0.0182` n `26`; metal avg `0.0613` n `20`; unknown avg `-0.0925` n `961`
- 1h: commodity avg `-0.0894` n `12`; crypto_alt avg `0.5871` n `234`; crypto_major avg `0.476` n `8`; equity avg `0.0901` n `141`; fx avg `0.008` n `6`; index avg `-0.0034` n `26`; metal avg `0.0795` n `20`; unknown avg `0.2852` n `961`
- 4h: commodity avg `-0.4345` n `12`; crypto_alt avg `1.778` n `234`; crypto_major avg `0.7991` n `8`; equity avg `0.777` n `141`; fx avg `-0.0047` n `6`; index avg `0.0988` n `26`; metal avg `0.1017` n `20`; unknown avg `0.5697` n `943`
- 24h: commodity avg `-0.7727` n `12`; crypto_alt avg `1.9507` n `234`; crypto_major avg `1.2478` n `8`; equity avg `0.0016` n `141`; fx avg `-0.0651` n `6`; index avg `-0.0139` n `26`; metal avg `-0.1727` n `20`; unknown avg `46.7015` n `808`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1865`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1584`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1583`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1377`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1259`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1163`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1102`, n `668`, weak_sample_signal
