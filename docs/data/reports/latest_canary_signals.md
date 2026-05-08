# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T10:52:20.474787+00:00`
- Correlation status: `ready`
- Asset price records: `639`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0743` n `12`; crypto_alt avg `0.1279` n `228`; crypto_major avg `0.1113` n `8`; equity avg `-0.0282` n `65`; fx avg `-0.0187` n `5`; index avg `-0.051` n `23`; metal avg `-0.0993` n `18`; unknown avg `0.0438` n `375`
- 1h: commodity avg `-0.1617` n `12`; crypto_alt avg `0.2488` n `228`; crypto_major avg `0.2284` n `8`; equity avg `0.1689` n `65`; fx avg `-0.0212` n `5`; index avg `-0.1055` n `23`; metal avg `0.2352` n `18`; unknown avg `0.0933` n `375`
- 4h: commodity avg `0.1337` n `12`; crypto_alt avg `0.8195` n `228`; crypto_major avg `0.6877` n `8`; equity avg `0.6008` n `65`; fx avg `0.0299` n `5`; index avg `0.0093` n `23`; metal avg `-0.0992` n `18`; unknown avg `0.6138` n `375`
- 24h: commodity avg `1.1102` n `12`; crypto_alt avg `1.2874` n `228`; crypto_major avg `-1.1101` n `8`; equity avg `-0.523` n `65`; fx avg `0.2324` n `5`; index avg `-0.555` n `23`; metal avg `-0.4096` n `18`; unknown avg `0.1075` n `355`

## Correlations

- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1407`, n `631`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1394`, n `631`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1091`, n `635`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `635`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0945`, n `635`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0934`, n `631`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0928`, n `635`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.081`, n `631`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0769`, n `631`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0747`, n `635`, weak_sample_signal
