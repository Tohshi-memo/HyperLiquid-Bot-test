# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-11T12:07:37.073066+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0082` n `12`; crypto_alt avg `0.0077` n `230`; crypto_major avg `0.0862` n `8`; equity avg `0.0325` n `113`; fx avg `0.0131` n `6`; index avg `0.0116` n `25`; metal avg `-0.0185` n `20`; unknown avg `-0.0346` n `785`
- 1h: commodity avg `0.0892` n `12`; crypto_alt avg `-0.0346` n `230`; crypto_major avg `0.0905` n `8`; equity avg `-0.1118` n `113`; fx avg `0.0017` n `6`; index avg `-0.0253` n `25`; metal avg `-0.045` n `20`; unknown avg `-0.1148` n `785`
- 4h: commodity avg `-0.4071` n `12`; crypto_alt avg `0.1635` n `230`; crypto_major avg `0.5885` n `8`; equity avg `0.3438` n `113`; fx avg `-0.0591` n `6`; index avg `0.0886` n `25`; metal avg `0.1796` n `20`; unknown avg `-0.0689` n `785`
- 24h: commodity avg `0.5401` n `12`; crypto_alt avg `-1.3387` n `230`; crypto_major avg `-0.5464` n `8`; equity avg `-0.6593` n `113`; fx avg `-0.0089` n `6`; index avg `0.1121` n `25`; metal avg `0.3976` n `20`; unknown avg `0.0808` n `752`

## Correlations

- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1889`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1806`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1386`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1152`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1124`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1027`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0994`, n `668`, weak_sample_signal
