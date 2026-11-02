# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T13:07:30.945579+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0523` n `13`; crypto_alt avg `-0.0037` n `238`; crypto_major avg `-0.0311` n `8`; equity avg `-0.1556` n `156`; fx avg `0.0063` n `6`; index avg `-0.0027` n `27`; metal avg `0.0192` n `20`; unknown avg `202.8683` n `1259`
- 1h: commodity avg `0.0179` n `13`; crypto_alt avg `-0.2467` n `238`; crypto_major avg `-0.2804` n `8`; equity avg `-0.4008` n `156`; fx avg `0.0148` n `6`; index avg `-0.0148` n `27`; metal avg `-0.0086` n `20`; unknown avg `2.956` n `1259`
- 4h: commodity avg `0.0623` n `13`; crypto_alt avg `-0.5444` n `238`; crypto_major avg `-0.6931` n `8`; equity avg `-0.6414` n `156`; fx avg `0.0038` n `6`; index avg `-0.0419` n `27`; metal avg `-0.0835` n `20`; unknown avg `5.8554` n `1252`
- 24h: commodity avg `-0.5069` n `13`; crypto_alt avg `-2.3836` n `238`; crypto_major avg `-0.7332` n `8`; equity avg `0.2756` n `156`; fx avg `0.2948` n `6`; index avg `0.254` n `27`; metal avg `-0.0207` n `20`; unknown avg `6.6126` n `1079`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1864`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1803`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1798`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1712`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1575`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.1542`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1437`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1375`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1279`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
