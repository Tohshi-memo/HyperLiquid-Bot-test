# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T08:52:29.340057+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1353` n `13`; crypto_alt avg `-0.1007` n `235`; crypto_major avg `-0.1753` n `8`; equity avg `-0.033` n `144`; fx avg `-0.0017` n `6`; index avg `0.0106` n `26`; metal avg `0.0122` n `20`; unknown avg `0.4761` n `1079`
- 1h: commodity avg `0.1766` n `13`; crypto_alt avg `-0.383` n `235`; crypto_major avg `-0.1207` n `8`; equity avg `-0.1152` n `144`; fx avg `0.0362` n `6`; index avg `-0.0241` n `26`; metal avg `0.0346` n `20`; unknown avg `-0.0902` n `997`
- 4h: commodity avg `0.1564` n `13`; crypto_alt avg `1.0071` n `235`; crypto_major avg `0.8775` n `8`; equity avg `0.022` n `144`; fx avg `0.0259` n `6`; index avg `0.0118` n `26`; metal avg `0.2881` n `20`; unknown avg `-0.3695` n `981`
- 24h: commodity avg `-0.1231` n `13`; crypto_alt avg `0.8317` n `235`; crypto_major avg `1.3167` n `8`; equity avg `0.2308` n `144`; fx avg `-0.0288` n `6`; index avg `-0.043` n `26`; metal avg `0.3076` n `20`; unknown avg `-0.3041` n `878`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.204`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1833`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1738`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.1514`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1409`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0895`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0766`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0761`, n `668`, weak_sample_signal
