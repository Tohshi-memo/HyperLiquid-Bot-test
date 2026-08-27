# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-27T07:37:28.514640+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0648` n `12`; crypto_alt avg `0.0302` n `231`; crypto_major avg `0.0258` n `8`; equity avg `-0.0243` n `127`; fx avg `-0.0005` n `6`; index avg `-0.0153` n `26`; metal avg `-0.0391` n `20`; unknown avg `0.0254` n `791`
- 1h: commodity avg `-0.0471` n `12`; crypto_alt avg `0.2117` n `231`; crypto_major avg `0.1269` n `8`; equity avg `0.2332` n `127`; fx avg `-0.0015` n `6`; index avg `0.0207` n `26`; metal avg `-0.1255` n `20`; unknown avg `0.0495` n `791`
- 4h: commodity avg `-0.1696` n `12`; crypto_alt avg `-0.0731` n `231`; crypto_major avg `0.0554` n `8`; equity avg `-0.0146` n `127`; fx avg `-0.0006` n `6`; index avg `-0.0569` n `26`; metal avg `-0.3206` n `20`; unknown avg `0.0352` n `775`
- 24h: commodity avg `0.3111` n `12`; crypto_alt avg `0.4265` n `231`; crypto_major avg `0.5209` n `8`; equity avg `1.6317` n `127`; fx avg `-0.0999` n `6`; index avg `0.2625` n `26`; metal avg `-0.4229` n `20`; unknown avg `0.4289` n `775`

## Correlations

- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1253`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1098`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0986`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0902`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0769`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0721`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0683`, n `668`, weak_sample_signal
