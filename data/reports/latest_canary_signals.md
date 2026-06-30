# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-30T07:22:30.961111+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0409` n `12`; crypto_alt avg `-0.0723` n `228`; crypto_major avg `-0.1093` n `8`; equity avg `-0.0556` n `88`; fx avg `0.0031` n `6`; index avg `-0.0178` n `23`; metal avg `0.0029` n `20`; unknown avg `0.0426` n `765`
- 1h: commodity avg `0.1809` n `12`; crypto_alt avg `-0.1373` n `228`; crypto_major avg `-0.0324` n `8`; equity avg `-0.0132` n `88`; fx avg `0.0207` n `6`; index avg `-0.0121` n `23`; metal avg `0.3964` n `20`; unknown avg `0.008` n `765`
- 4h: commodity avg `0.0067` n `12`; crypto_alt avg `-0.3469` n `228`; crypto_major avg `-0.5798` n `8`; equity avg `0.0859` n `88`; fx avg `0.0392` n `6`; index avg `0.0365` n `23`; metal avg `0.6066` n `20`; unknown avg `7.0255` n `737`
- 24h: commodity avg `-0.1067` n `12`; crypto_alt avg `-0.4517` n `228`; crypto_major avg `0.6171` n `8`; equity avg `1.7187` n `88`; fx avg `0.1555` n `6`; index avg `0.1857` n `23`; metal avg `-0.0516` n `20`; unknown avg `9.397` n `734`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1215`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0953`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0837`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.076`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0657`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0619`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.061`, n `668`, weak_sample_signal
