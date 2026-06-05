# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-05T04:22:25.216227+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `-1.6752` - Crypto majors and equity perps are diverging; watch lead/lag rotation.
- 4h_index_leads_crypto: score `1.5233` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0407` n `12`; crypto_alt avg `-0.1637` n `228`; crypto_major avg `-0.4602` n `8`; equity avg `-0.0162` n `74`; fx avg `0.002` n `6`; index avg `-0.0043` n `23`; metal avg `-0.0317` n `18`; unknown avg `-0.4171` n `424`
- 1h: commodity avg `-0.029` n `12`; crypto_alt avg `0.1059` n `228`; crypto_major avg `-0.1878` n `8`; equity avg `-0.1412` n `74`; fx avg `0.0128` n `6`; index avg `-0.0832` n `23`; metal avg `0.1377` n `18`; unknown avg `0.4841` n `424`
- 4h: commodity avg `0.0209` n `12`; crypto_alt avg `-2.0983` n `228`; crypto_major avg `-1.6931` n `8`; equity avg `-0.0179` n `74`; fx avg `0.0807` n `6`; index avg `-0.1698` n `23`; metal avg `-0.4203` n `18`; unknown avg `0.2015` n `424`
- 24h: commodity avg `-0.2041` n `12`; crypto_alt avg `-6.4341` n `228`; crypto_major avg `-5.7603` n `8`; equity avg `-1.7311` n `73`; fx avg `0.1971` n `6`; index avg `-0.5742` n `23`; metal avg `-0.7382` n `18`; unknown avg `-0.9136` n `402`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1201`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1002`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0963`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0899`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0749`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0728`, n `668`, weak_sample_signal
