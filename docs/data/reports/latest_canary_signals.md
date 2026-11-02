# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T09:37:37.367670+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0257` n `13`; crypto_alt avg `-0.2314` n `238`; crypto_major avg `-0.2288` n `8`; equity avg `-0.0644` n `156`; fx avg `-0.0164` n `6`; index avg `-0.0059` n `27`; metal avg `-0.0013` n `20`; unknown avg `1.8203` n `1264`
- 1h: commodity avg `0.0233` n `13`; crypto_alt avg `-0.3222` n `238`; crypto_major avg `-0.2318` n `8`; equity avg `0.0693` n `156`; fx avg `0.0338` n `6`; index avg `0.0346` n `27`; metal avg `-0.0135` n `20`; unknown avg `2.1463` n `1256`
- 4h: commodity avg `-0.1084` n `13`; crypto_alt avg `-1.1679` n `238`; crypto_major avg `-0.6455` n `8`; equity avg `-0.2104` n `156`; fx avg `0.0923` n `6`; index avg `-0.0523` n `27`; metal avg `-0.1149` n `20`; unknown avg `2.7715` n `1152`
- 24h: commodity avg `-0.5749` n `13`; crypto_alt avg `-1.9486` n `238`; crypto_major avg `-0.387` n `8`; equity avg `0.9225` n `156`; fx avg `0.2863` n `6`; index avg `0.3055` n `27`; metal avg `0.0808` n `20`; unknown avg `4.918` n `1065`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1808`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.173`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1725`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1652`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1484`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1352`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1313`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1184`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
