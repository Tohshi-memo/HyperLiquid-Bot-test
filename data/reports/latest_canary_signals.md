# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T07:22:32.729131+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0295` n `12`; crypto_alt avg `0.0526` n `230`; crypto_major avg `0.0525` n `8`; equity avg `0.0413` n `112`; fx avg `-0.0132` n `6`; index avg `0.0164` n `25`; metal avg `-0.0275` n `20`; unknown avg `0.0098` n `785`
- 1h: commodity avg `0.1026` n `12`; crypto_alt avg `0.0824` n `230`; crypto_major avg `0.2016` n `8`; equity avg `0.0956` n `112`; fx avg `0.0178` n `6`; index avg `0.0178` n `25`; metal avg `0.0257` n `20`; unknown avg `0.0702` n `785`
- 4h: commodity avg `0.0065` n `12`; crypto_alt avg `0.2587` n `230`; crypto_major avg `0.3105` n `8`; equity avg `0.2262` n `112`; fx avg `0.0747` n `6`; index avg `0.0349` n `25`; metal avg `0.1663` n `20`; unknown avg `57.1899` n `753`
- 24h: commodity avg `0.3872` n `12`; crypto_alt avg `1.0916` n `230`; crypto_major avg `0.3046` n `8`; equity avg `-0.0777` n `112`; fx avg `0.1948` n `6`; index avg `0.0643` n `25`; metal avg `0.0051` n `20`; unknown avg `56.9029` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1902`, n `669`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1417`, n `669`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1373`, n `669`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1341`, n `669`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1191`, n `669`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.118`, n `669`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1171`, n `669`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1087`, n `669`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `669`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0981`, n `669`, weak_sample_signal
