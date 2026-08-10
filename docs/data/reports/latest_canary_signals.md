# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T11:07:29.603530+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.014` n `12`; crypto_alt avg `-0.1372` n `230`; crypto_major avg `-0.0963` n `8`; equity avg `-0.328` n `113`; fx avg `0.003` n `6`; index avg `-0.0398` n `25`; metal avg `-0.0397` n `20`; unknown avg `-0.0357` n `784`
- 1h: commodity avg `0.1107` n `12`; crypto_alt avg `-0.005` n `230`; crypto_major avg `-0.0106` n `8`; equity avg `-0.3683` n `113`; fx avg `-0.0126` n `6`; index avg `-0.0523` n `25`; metal avg `-0.0421` n `20`; unknown avg `0.0118` n `784`
- 4h: commodity avg `0.1775` n `12`; crypto_alt avg `-0.0912` n `230`; crypto_major avg `-0.2625` n `8`; equity avg `-0.4161` n `113`; fx avg `0.015` n `6`; index avg `-0.0416` n `25`; metal avg `-0.1987` n `20`; unknown avg `0.0135` n `784`
- 24h: commodity avg `0.5176` n `12`; crypto_alt avg `0.8028` n `230`; crypto_major avg `-0.0899` n `8`; equity avg `-0.4616` n `113`; fx avg `0.2224` n `6`; index avg `0.0204` n `25`; metal avg `-0.1935` n `20`; unknown avg `57.0026` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.184`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.145`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1324`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1181`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1149`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0977`, n `668`, weak_sample_signal
