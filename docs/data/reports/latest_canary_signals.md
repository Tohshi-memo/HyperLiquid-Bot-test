# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-14T14:22:26.587650+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0091` n `12`; crypto_alt avg `0.025` n `230`; crypto_major avg `-0.096` n `8`; equity avg `-0.5199` n `114`; fx avg `0.0116` n `6`; index avg `-0.0895` n `25`; metal avg `-0.0375` n `20`; unknown avg `0.0268` n `786`
- 1h: commodity avg `0.1254` n `12`; crypto_alt avg `-0.038` n `230`; crypto_major avg `-0.1399` n `8`; equity avg `-0.2484` n `114`; fx avg `0.0523` n `6`; index avg `-0.047` n `25`; metal avg `0.0795` n `20`; unknown avg `-0.2723` n `786`
- 4h: commodity avg `0.0431` n `12`; crypto_alt avg `0.0112` n `230`; crypto_major avg `-0.4454` n `8`; equity avg `-0.289` n `114`; fx avg `0.0574` n `6`; index avg `-0.0571` n `25`; metal avg `0.2055` n `20`; unknown avg `2.821` n `786`
- 24h: commodity avg `0.2296` n `12`; crypto_alt avg `-0.914` n `230`; crypto_major avg `-1.4186` n `8`; equity avg `-0.1676` n `114`; fx avg `0.0393` n `6`; index avg `0.0282` n `25`; metal avg `0.1757` n `20`; unknown avg `0.2755` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.1949`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1812`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.18`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1687`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1596`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1543`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1504`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1484`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1345`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.133`, n `668`, weak_sample_signal
