# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T02:37:12.311081+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-2.5293` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_index_leads_crypto: score `1.3648` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0095` n `12`; crypto_alt avg `0.034` n `228`; crypto_major avg `-0.1012` n `8`; equity avg `0.1721` n `66`; fx avg `-0.0244` n `5`; index avg `0.0149` n `23`; metal avg `0.1059` n `18`; unknown avg `-0.1865` n `383`
- 1h: commodity avg `-0.1935` n `12`; crypto_alt avg `0.6591` n `228`; crypto_major avg `0.2064` n `8`; equity avg `0.9302` n `66`; fx avg `0.0138` n `5`; index avg `0.2701` n `23`; metal avg `0.62` n `18`; unknown avg `-0.1852` n `383`
- 4h: commodity avg `0.8696` n `12`; crypto_alt avg `-1.3887` n `228`; crypto_major avg `-1.6597` n `8`; equity avg `-0.269` n `66`; fx avg `0.0942` n `5`; index avg `-0.2949` n `23`; metal avg `-0.8738` n `18`; unknown avg `0.1746` n `383`
- 24h: commodity avg `2.701` n `12`; crypto_alt avg `-10.8044` n `228`; crypto_major avg `-3.271` n `8`; equity avg `-2.7934` n `65`; fx avg `-0.0788` n `5`; index avg `-1.75` n `23`; metal avg `-6.1862` n `18`; unknown avg `550.2254` n `367`

## Correlations

- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1411`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1215`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1101`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1008`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0974`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0906`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0865`, n `668`, weak_sample_signal
