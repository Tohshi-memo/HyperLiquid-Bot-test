# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-25T13:52:31.987058+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.4093` n `12`; crypto_alt avg `0.0559` n `230`; crypto_major avg `0.0635` n `8`; equity avg `0.02` n `100`; fx avg `-0.0037` n `6`; index avg `0.0203` n `25`; metal avg `0.0186` n `20`; unknown avg `0.0745` n `774`
- 1h: commodity avg `-0.4244` n `12`; crypto_alt avg `0.2033` n `230`; crypto_major avg `0.2267` n `8`; equity avg `-0.0107` n `100`; fx avg `0.0017` n `6`; index avg `0.0222` n `25`; metal avg `0.0167` n `20`; unknown avg `0.0554` n `774`
- 4h: commodity avg `-0.5064` n `12`; crypto_alt avg `0.2248` n `230`; crypto_major avg `0.1664` n `8`; equity avg `0.0432` n `100`; fx avg `-0.0057` n `6`; index avg `0.0169` n `25`; metal avg `0.0044` n `20`; unknown avg `-0.0019` n `774`
- 24h: commodity avg `-0.6173` n `12`; crypto_alt avg `0.0967` n `230`; crypto_major avg `0.425` n `8`; equity avg `-0.8243` n `100`; fx avg `-0.0125` n `6`; index avg `0.0003` n `25`; metal avg `-0.0117` n `20`; unknown avg `13.3319` n `757`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1636`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1572`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1295`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1277`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1246`, n `666`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.117`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1159`, n `666`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1083`, n `666`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1069`, n `668`, weak_sample_signal
