# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-14T13:37:32.445913+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0102` n `12`; crypto_alt avg `-0.1253` n `228`; crypto_major avg `0.0158` n `8`; equity avg `-0.0818` n `74`; fx avg `-0.0046` n `6`; index avg `-0.0441` n `23`; metal avg `-0.024` n `18`; unknown avg `0.0683` n `645`
- 1h: commodity avg `0.0902` n `12`; crypto_alt avg `-0.3452` n `228`; crypto_major avg `-0.0419` n `8`; equity avg `-0.1319` n `74`; fx avg `-0.0207` n `6`; index avg `-0.0071` n `23`; metal avg `-0.0852` n `18`; unknown avg `0.3075` n `645`
- 4h: commodity avg `0.2989` n `12`; crypto_alt avg `-0.8158` n `228`; crypto_major avg `-0.2364` n `8`; equity avg `-0.0604` n `74`; fx avg `0.0253` n `6`; index avg `0.1178` n `23`; metal avg `-0.1367` n `18`; unknown avg `0.6152` n `645`
- 24h: commodity avg `-0.1414` n `12`; crypto_alt avg `-0.9398` n `228`; crypto_major avg `-0.2202` n `8`; equity avg `0.5152` n `74`; fx avg `-0.0074` n `6`; index avg `0.0946` n `23`; metal avg `-0.0452` n `18`; unknown avg `-1.0145` n `592`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.104`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0999`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0822`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.0676`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0643`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0617`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.0577`, n `668`, weak_sample_signal
