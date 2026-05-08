# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T06:07:19.047340+00:00`
- Correlation status: `ready`
- Asset price records: `620`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.02` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.1694` n `12`; crypto_alt avg `-0.3999` n `228`; crypto_major avg `-0.2166` n `8`; equity avg `0.0117` n `65`; fx avg `0.0176` n `5`; index avg `0.0029` n `23`; metal avg `0.2851` n `18`; unknown avg `-0.0849` n `355`
- 1h: commodity avg `-0.2174` n `12`; crypto_alt avg `-0.4309` n `228`; crypto_major avg `-0.1206` n `8`; equity avg `0.0961` n `65`; fx avg `0.038` n `5`; index avg `0.0578` n `23`; metal avg `0.6536` n `18`; unknown avg `0.0437` n `355`
- 4h: commodity avg `-0.3973` n `12`; crypto_alt avg `0.3778` n `228`; crypto_major avg `-0.0267` n `8`; equity avg `0.3172` n `65`; fx avg `0.0862` n `5`; index avg `0.0756` n `23`; metal avg `0.5244` n `18`; unknown avg `0.4674` n `355`
- 24h: commodity avg `0.3691` n `12`; crypto_alt avg `0.9136` n `228`; crypto_major avg `-1.7686` n `8`; equity avg `-1.0318` n `65`; fx avg `0.2579` n `5`; index avg `-0.6186` n `23`; metal avg `0.8993` n `18`; unknown avg `-0.2594` n `355`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1233`, n `612`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1231`, n `612`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1167`, n `616`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1135`, n `616`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1091`, n `616`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0968`, n `616`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0862`, n `612`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0822`, n `612`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0806`, n `612`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.072`, n `616`, weak_sample_signal
