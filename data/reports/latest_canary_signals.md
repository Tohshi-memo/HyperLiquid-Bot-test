# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-31T15:37:31.053923+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0151` n `13`; crypto_alt avg `0.2511` n `238`; crypto_major avg `0.2118` n `8`; equity avg `0.0236` n `156`; fx avg `-0.0036` n `6`; index avg `-0.0017` n `27`; metal avg `0.0034` n `20`; unknown avg `0.3528` n `1254`
- 1h: commodity avg `0.0082` n `13`; crypto_alt avg `0.8131` n `238`; crypto_major avg `0.3497` n `8`; equity avg `0.088` n `156`; fx avg `0.0038` n `6`; index avg `0.0028` n `27`; metal avg `0.0178` n `20`; unknown avg `0.0932` n `1248`
- 4h: commodity avg `-0.0822` n `13`; crypto_alt avg `0.9578` n `238`; crypto_major avg `0.1762` n `8`; equity avg `0.0852` n `156`; fx avg `0.0122` n `6`; index avg `-0.0045` n `27`; metal avg `0.0229` n `20`; unknown avg `-0.0636` n `1244`
- 24h: commodity avg `-0.26` n `13`; crypto_alt avg `1.3093` n `238`; crypto_major avg `-0.0979` n `8`; equity avg `0.0475` n `156`; fx avg `0.0196` n `6`; index avg `-0.071` n `27`; metal avg `-0.0212` n `20`; unknown avg `0.5944` n `1089`

## Correlations

- market_context_score -> metal_forward_1h_return_pct: corr `0.1555`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1512`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1436`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.139`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1255`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1107`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0946`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0913`, n `668`, weak_sample_signal
