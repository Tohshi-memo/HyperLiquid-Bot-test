# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-25T01:22:25.876436+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6604` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0427` n `12`; crypto_alt avg `-0.3019` n `231`; crypto_major avg `-0.1406` n `8`; equity avg `-0.0786` n `122`; fx avg `0.0042` n `6`; index avg `-0.0238` n `25`; metal avg `-0.0401` n `20`; unknown avg `-0.0628` n `794`
- 1h: commodity avg `0.0329` n `12`; crypto_alt avg `0.5649` n `231`; crypto_major avg `0.7945` n `8`; equity avg `0.256` n `122`; fx avg `0.0102` n `6`; index avg `0.0397` n `25`; metal avg `0.0102` n `20`; unknown avg `2.0943` n `794`
- 4h: commodity avg `0.0333` n `12`; crypto_alt avg `0.5528` n `231`; crypto_major avg `1.5209` n `8`; equity avg `-0.1395` n `122`; fx avg `0.028` n `6`; index avg `-0.0682` n `25`; metal avg `0.1333` n `20`; unknown avg `0.2522` n `794`
- 24h: commodity avg `0.167` n `12`; crypto_alt avg `0.5306` n `231`; crypto_major avg `1.5779` n `8`; equity avg `-2.6331` n `122`; fx avg `-0.0212` n `6`; index avg `-0.4025` n `25`; metal avg `0.2908` n `20`; unknown avg `0.9317` n `777`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1083`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0876`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0681`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.0598`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0466`, n `668`, weak_sample_signal
