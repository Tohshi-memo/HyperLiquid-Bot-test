# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-01T10:52:19.533016+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0112` n `12`; crypto_alt avg `0.4349` n `228`; crypto_major avg `0.2736` n `8`; equity avg `-0.0572` n `69`; fx avg `-0.0043` n `6`; index avg `-0.0057` n `23`; metal avg `-0.0417` n `18`; unknown avg `2.1518` n `422`
- 1h: commodity avg `-0.1055` n `12`; crypto_alt avg `0.1244` n `228`; crypto_major avg `-0.0867` n `8`; equity avg `0.1595` n `69`; fx avg `-0.0019` n `6`; index avg `0.1135` n `23`; metal avg `0.2567` n `18`; unknown avg `2.8017` n `422`
- 4h: commodity avg `-0.0564` n `12`; crypto_alt avg `-0.2353` n `228`; crypto_major avg `-0.1026` n `8`; equity avg `-0.1606` n `69`; fx avg `0.0332` n `6`; index avg `-0.3771` n `23`; metal avg `0.3011` n `18`; unknown avg `2.7309` n `422`
- 24h: commodity avg `1.0225` n `12`; crypto_alt avg `-0.1919` n `228`; crypto_major avg `-0.3461` n `8`; equity avg `-0.0604` n `69`; fx avg `-0.0112` n `6`; index avg `0.5367` n `23`; metal avg `0.3177` n `18`; unknown avg `4.4523` n `411`

## Correlations

- flow_alert_score -> metal_forward_1h_return_pct: corr `0.2864`, n `668`, moderate_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.206`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1527`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1225`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
