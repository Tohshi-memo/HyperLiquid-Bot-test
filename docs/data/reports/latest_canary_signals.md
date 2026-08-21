# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T21:37:22.933667+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_metal_divergence: score `1.7495` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.
- 4h_crypto_equity_divergence: score `1.7105` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.0044` n `12`; crypto_alt avg `0.3094` n `230`; crypto_major avg `0.4958` n `8`; equity avg `0.0049` n `121`; fx avg `-0.001` n `6`; index avg `0.0046` n `25`; metal avg `0.0215` n `20`; unknown avg `-0.115` n `793`
- 1h: commodity avg `0.004` n `12`; crypto_alt avg `1.0418` n `230`; crypto_major avg `1.4268` n `8`; equity avg `-0.0146` n `121`; fx avg `0.0144` n `6`; index avg `0.0014` n `25`; metal avg `0.0139` n `20`; unknown avg `-0.2031` n `793`
- 4h: commodity avg `-0.0973` n `12`; crypto_alt avg `1.0657` n `230`; crypto_major avg `1.6648` n `8`; equity avg `-0.0457` n `121`; fx avg `0.0099` n `6`; index avg `-0.0188` n `25`; metal avg `-0.0847` n `20`; unknown avg `-0.3469` n `793`
- 24h: commodity avg `0.1725` n `12`; crypto_alt avg `8.0315` n `230`; crypto_major avg `6.107` n `8`; equity avg `0.8624` n `121`; fx avg `-0.0648` n `6`; index avg `0.0992` n `25`; metal avg `0.5228` n `20`; unknown avg `1.1692` n `777`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.2175`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1859`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1847`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1815`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.108`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0951`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0862`, n `668`, weak_sample_signal
