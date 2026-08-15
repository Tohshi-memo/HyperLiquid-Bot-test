# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T03:52:53.669470+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0332` n `12`; crypto_alt avg `-0.0447` n `230`; crypto_major avg `-0.0196` n `8`; equity avg `0.006` n `114`; fx avg `-0.0164` n `6`; index avg `-0.0081` n `25`; metal avg `-0.002` n `20`; unknown avg `0.1589` n `791`
- 1h: commodity avg `0.0096` n `12`; crypto_alt avg `-0.1246` n `230`; crypto_major avg `0.0014` n `8`; equity avg `0.035` n `114`; fx avg `-0.0331` n `6`; index avg `-0.0031` n `25`; metal avg `-0.0246` n `20`; unknown avg `0.0247` n `791`
- 4h: commodity avg `-0.0218` n `12`; crypto_alt avg `-0.0415` n `230`; crypto_major avg `0.1988` n `8`; equity avg `0.0581` n `114`; fx avg `0.0578` n `6`; index avg `0.0014` n `25`; metal avg `-0.0093` n `20`; unknown avg `0.2058` n `791`
- 24h: commodity avg `0.1863` n `12`; crypto_alt avg `0.3653` n `230`; crypto_major avg `-0.1159` n `8`; equity avg `-0.1185` n `114`; fx avg `0.1697` n `6`; index avg `-0.0357` n `25`; metal avg `0.3995` n `20`; unknown avg `0.0478` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2188`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1895`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1816`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1699`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.168`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1524`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1507`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1485`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1456`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1416`, n `668`, weak_sample_signal
