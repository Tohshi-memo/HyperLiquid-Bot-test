# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-30T18:52:23.599106+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0407` n `12`; crypto_alt avg `0.0888` n `228`; crypto_major avg `-0.0092` n `8`; equity avg `0.0193` n `69`; fx avg `-0.0006` n `6`; index avg `-0.0132` n `23`; metal avg `-0.0075` n `18`; unknown avg `-0.0393` n `421`
- 1h: commodity avg `0.0608` n `12`; crypto_alt avg `0.315` n `228`; crypto_major avg `0.0574` n `8`; equity avg `0.0566` n `69`; fx avg `-0.0015` n `6`; index avg `-0.0057` n `23`; metal avg `-0.0114` n `18`; unknown avg `-0.1269` n `421`
- 4h: commodity avg `-0.3935` n `12`; crypto_alt avg `0.4725` n `228`; crypto_major avg `0.6905` n `8`; equity avg `-0.1348` n `69`; fx avg `-0.0215` n `6`; index avg `-0.1675` n `23`; metal avg `0.0368` n `18`; unknown avg `-0.2564` n `421`
- 24h: commodity avg `-0.0843` n `12`; crypto_alt avg `1.8832` n `228`; crypto_major avg `2.9277` n `8`; equity avg `1.2487` n `69`; fx avg `-0.0024` n `6`; index avg `0.163` n `23`; metal avg `-0.0573` n `18`; unknown avg `0.206` n `401`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1893`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1548`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1471`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1334`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1231`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1194`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1164`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1112`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
