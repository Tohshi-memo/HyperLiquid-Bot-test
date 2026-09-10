# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T18:37:37.189516+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0706` n `12`; crypto_alt avg `-0.0376` n `233`; crypto_major avg `-0.0282` n `8`; equity avg `-0.0173` n `135`; fx avg `0.0001` n `6`; index avg `-0.0086` n `26`; metal avg `-0.0728` n `20`; unknown avg `-0.3261` n `797`
- 1h: commodity avg `0.0424` n `12`; crypto_alt avg `-0.4441` n `233`; crypto_major avg `-0.4712` n `8`; equity avg `-0.2225` n `135`; fx avg `-0.009` n `6`; index avg `-0.0356` n `26`; metal avg `-0.1759` n `20`; unknown avg `0.7242` n `795`
- 4h: commodity avg `0.5994` n `12`; crypto_alt avg `-0.3916` n `233`; crypto_major avg `-0.4075` n `8`; equity avg `-0.8245` n `135`; fx avg `0.0231` n `6`; index avg `-0.1496` n `26`; metal avg `-0.3636` n `20`; unknown avg `0.0567` n `760`
- 24h: commodity avg `1.0069` n `12`; crypto_alt avg `-4.5952` n `233`; crypto_major avg `-3.6894` n `8`; equity avg `-2.1495` n `135`; fx avg `0.0937` n `6`; index avg `-0.3387` n `26`; metal avg `-1.3479` n `20`; unknown avg `-0.0381` n `660`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1322`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1261`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.1088`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1057`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0936`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `0.0881`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0869`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0833`, n `668`, weak_sample_signal
