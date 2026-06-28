# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-28T16:52:35.073205+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0652` n `12`; crypto_alt avg `0.132` n `228`; crypto_major avg `-0.0063` n `8`; equity avg `0.0431` n `88`; fx avg `0.0042` n `6`; index avg `-0.0111` n `23`; metal avg `0.0046` n `20`; unknown avg `-0.0108` n `764`
- 1h: commodity avg `0.1165` n `12`; crypto_alt avg `-0.6337` n `228`; crypto_major avg `-0.6734` n `8`; equity avg `-0.0281` n `88`; fx avg `0.0042` n `6`; index avg `-0.0137` n `23`; metal avg `-0.0011` n `20`; unknown avg `-0.3232` n `764`
- 4h: commodity avg `0.206` n `12`; crypto_alt avg `-0.3762` n `228`; crypto_major avg `-0.721` n `8`; equity avg `-0.0159` n `88`; fx avg `0.0003` n `6`; index avg `-0.0167` n `23`; metal avg `-0.0579` n `20`; unknown avg `0.1253` n `764`
- 24h: commodity avg `0.4122` n `12`; crypto_alt avg `-1.3716` n `228`; crypto_major avg `-2.2592` n `8`; equity avg `0.0162` n `88`; fx avg `0.0017` n `6`; index avg `-0.0607` n `23`; metal avg `-0.0842` n `20`; unknown avg `14.6513` n `690`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1908`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1849`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1354`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.127`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0919`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0854`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0818`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
