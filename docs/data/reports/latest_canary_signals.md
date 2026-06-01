# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T07:21:39.185433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.5584` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.119` n `12`; crypto_alt avg `-0.1933` n `228`; crypto_major avg `-0.3105` n `8`; equity avg `-0.0593` n `69`; fx avg `0.0124` n `6`; index avg `0.1755` n `23`; metal avg `-0.0064` n `18`; unknown avg `0.2018` n `422`
- 1h: commodity avg `0.1705` n `12`; crypto_alt avg `-0.2753` n `228`; crypto_major avg `-0.3056` n `8`; equity avg `-0.0902` n `69`; fx avg `0.0469` n `6`; index avg `0.5534` n `23`; metal avg `-0.0134` n `18`; unknown avg `0.0577` n `422`
- 4h: commodity avg `0.4477` n `12`; crypto_alt avg `-1.8307` n `228`; crypto_major avg `-1.1979` n `8`; equity avg `-0.2167` n `69`; fx avg `-0.055` n `6`; index avg `0.3605` n `23`; metal avg `-0.0833` n `18`; unknown avg `-0.2689` n `412`
- 24h: commodity avg `1.2664` n `12`; crypto_alt avg `-0.2403` n `228`; crypto_major avg `-0.8419` n `8`; equity avg `0.165` n `69`; fx avg `-0.0223` n `6`; index avg `1.1407` n `23`; metal avg `0.1051` n `18`; unknown avg `1.5916` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2874`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2183`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.2058`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1544`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1496`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1044`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1022`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0864`, n `668`, weak_sample_signal
