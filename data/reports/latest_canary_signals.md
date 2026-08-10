# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T08:02:56.597164+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0209` n `12`; crypto_alt avg `0.0484` n `230`; crypto_major avg `0.056` n `8`; equity avg `0.1331` n `112`; fx avg `-0.0059` n `6`; index avg `0.0208` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.0046` n `785`
- 1h: commodity avg `-0.0742` n `12`; crypto_alt avg `0.0907` n `230`; crypto_major avg `0.0939` n `8`; equity avg `0.271` n `112`; fx avg `-0.0046` n `6`; index avg `0.0477` n `25`; metal avg `-0.0331` n `20`; unknown avg `0.0063` n `785`
- 4h: commodity avg `-0.0803` n `12`; crypto_alt avg `0.3982` n `230`; crypto_major avg `0.5139` n `8`; equity avg `0.4182` n `112`; fx avg `0.0947` n `6`; index avg `0.0696` n `25`; metal avg `0.1629` n `20`; unknown avg `57.2135` n `753`
- 24h: commodity avg `0.3089` n `12`; crypto_alt avg `0.8721` n `230`; crypto_major avg `0.1864` n `8`; equity avg `0.1598` n `112`; fx avg `0.1995` n `6`; index avg `0.0867` n `25`; metal avg `-0.0145` n `20`; unknown avg `56.8992` n `753`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1445`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1369`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1204`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1193`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1182`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1132`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0998`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0979`, n `668`, weak_sample_signal
